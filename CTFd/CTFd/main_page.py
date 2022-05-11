from flask import Blueprint, render_template

from CTFd.utils import config
from CTFd.utils.config.visibility import scores_visible
from CTFd.utils.decorators.visibility import check_score_visibility
from CTFd.utils.helpers import get_infos
from CTFd.utils.scores import get_standings
from CTFd.utils.user import is_admin

main_page = Blueprint("main_page", __name__)


@main_page.route("/main_page")
@check_score_visibility
def listing():
    infos = get_infos()

    if config.is_main_page_frozen():
        infos.append("main_page has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")

    standings = get_standings()
    return render_template("main_page.html", standings=standings, infos=infos)
