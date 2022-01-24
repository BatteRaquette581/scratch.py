import requests
from exceptions import InvalidLimit
class User:
  """
  Class to fetch information about an user.
  """
  def __init__(self, user):
    self.user = user
    #self.raw corresponds to the raw_json response by the Scratch API.
    self.raw = requests.get(f"https://api.scratch.mit.edu/users/{self.user}").json()
    #Variable assignments.
    self.id = self.raw["id"]
    self.username = self.raw["username"]
    self.scratchemployee = self.raw["scratchteam"]
    self.scratchteam = self.scratchemployee
    self.join_date = self.raw["history"]["joined"]
    self.profile = self.raw["profile"]
    self.pfp = self.profile["images"]
    self.about_me = self.profile["status"]
    self.bio = self.profile["bio"]
    self.what_im_working_on = self.bio
    self.country = self.profile["country"]
  #__enter__ and __exit__ functions are made to be used with "with" statements.
  def __enter__(self):
    return self.raw
  def __exit__(self,*args):
    return self.raw
  def fetch_favorites(self,limit=40):
    """
    Get favorites that the user put. (project IDs)
    """
    if 40 < limit:
      raise InvalidLimit("Limit cannot be bigger than 40 or be smaller than 1.")
    limit = str(limit)
    response = requests.get(f"https://api.scratch.mit.edu/users/{self.user}/favorites/?limit="+limit).json()
    ids = []
    for i in response:
      ids.append(i["id"])
    return ids
  def fetch_followers(self,limit=40):
    """
    Get users that followed the user. (user IDs)
    """
    if 40 < limit:
      raise InvalidLimit("Limit cannot be bigger than 40 or be smaller than 1.")
    limit = str(limit)
    response = requests.get(f"https://api.scratch.mit.edu/users/{self.user}/followers/?limit="+limit).json()
    ids = []
    for i in response:
      ids.append(i["id"])
    return ids
  def fetch_following(self,limit=40):
    """
    Get the users that the user followed. (user IDs)
    """
    if 40 < limit:
      raise InvalidLimit("Limit cannot be bigger than 40 or be smaller than 1.")
    limit = str(limit)
    response = requests.get(f"https://api.scratch.mit.edu/users/{self.user}/following/?limit="+limit).json()
    ids = []
    for i in response:
      ids.append(i["id"])
    return ids