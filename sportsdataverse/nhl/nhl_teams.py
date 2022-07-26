import pandas as pd
import json
from sportsdataverse.dl_utils import download
from urllib.error import URLError, HTTPError, ContentTooShortError

def espn_nhl_teams() -> pd.DataFrame:
    """espn_nhl_teams - look up NHL teams

    Returns:
        pd.DataFrame: Pandas dataframe containing teams for the requested league.
    """
    ev = pd.DataFrame()
    url = "http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams?limit=1000"
    resp = download(url=url)
    if resp is not None:
        events_txt = json.loads(resp)

        teams = events_txt.get('sports')[0].get('leagues')[0].get('teams')
        del_keys = ['record', 'links']
        for team in teams:
            for k in del_keys:
                team.get('team').pop(k, None)
        teams = pd.json_normalize(teams, sep='_')
    teams.columns = [underscore(c) for c in teams.columns.tolist()]
    return teams

