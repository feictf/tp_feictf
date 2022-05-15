import datetime

import docker
from flask import render_template
from sqlalchemy.sql import or_, and_
from CTFd.models import db, Users, Solves, Challenges, Teams
from CTFd.cache import cache
from CTFd.utils.helpers import get_infos
from CTFd.utils.user import get_current_user

from ..utils import active_dojo_id, dojo_modules

def module_challenges(module, user_id=None):
    solves = db.func.count(Solves.id).label("solves")
    solved = db.func.max(Solves.user_id == user_id).label("solved")
    challenges = (
        db.session.query(Challenges.id, Challenges.name, Challenges.category, solves, solved)
        .filter(Challenges.state == "visible",
                or_(*(
                    and_(Challenges.category == module_challenge["category"],
                         Challenges.name.in_(module_challenge["names"]))
                    if module_challenge.get("names") else
                    Challenges.category == module_challenge["category"]
                    for module_challenge in module.get("challenges", [])
                ), False))
        .outerjoin(Solves, Solves.challenge_id == Challenges.id)
        .group_by(Challenges.id)
    ).all()
    return challenges

@cache.memoize(timeout=60)
def get_stats():
    docker_client = docker.from_env()
    containers = docker_client.containers.list(filters=dict(name="user_"), ignore_removed=True)
    now = datetime.datetime.now()
    active = 0.0
    for container in containers:
        created = container.attrs["Created"].split(".")[0]
        uptime = now - datetime.datetime.fromisoformat(created)
        hours = max(uptime.seconds // (60 * 60), 1)
        active += 1 / hours

    return {
        "active": int(active),
        "users": int(Users.query.count()),
        "challenges": int(Challenges.query.count()),
        "solves": int(Solves.query.count()),
        "teams": int(Teams.query.count()),
    }


def scoreboard_override():
    infos = get_infos()
    stats = get_stats()

    user = get_current_user()
    dojo_id = active_dojo_id(user.id) if user else None
    modules = dojo_modules(dojo_id)

    for module in modules:
        challenges = module_challenges(module, user.id if user else None)
        module["challenges_count"] = len(challenges)
        module["challenges_solved"] = sum(1 for challenge in challenges if challenge.solved)


    return render_template(
        "scoreboard.html",
        infos=infos,
        stats=stats,
        modules=modules,
    )
