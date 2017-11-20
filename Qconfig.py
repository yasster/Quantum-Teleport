# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal 
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "b899b6b61a9f873fa9e7cfd638a05c20621faab6f9d68f48dfe34a0c69d277137e1edeea270b18a3bf9c94e43599fad93a0022e24274ef296fa65ba9e489659a"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")
