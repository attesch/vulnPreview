# An example to get the remaining rate limit using the Github GraphQL API.

import requests
import simplejson as json
import argparse

parser = argparse.ArgumentParser(description="Beta GraphQL query for Github Vulnerabilities.")
parser.add_argument('--owner', help='owner or organization name where repository is located')
parser.add_argument('--repository', help='github repository to check for known vulnerabilities')
parser.add_argument('--token', help='github token that can query repo')
args = parser.parse_args()


#myAPIToken=args.token
#githubv4 = 'https://api.github.com/graphql'

# Headers need to authorize the request, and enable the Preview API for Vulnerabilities.
# https://developer.github.com/v4/previews/#repository-vulnerability-alerts
headers ={ 
  "Authorization": "",
  "Accept": "application/vnd.github.vixen-preview+json"
}
headers['Authorization']="Bearer {}".format(args.token)

#print (headers)

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
{
  repository (name: MYREPO, owner: MYORG) {
    name
    vulnerabilityAlerts (first: 50) {
      totalCount
      edges {
        node {
          id
          packageName
          securityVulnerability {
            package {name}
            firstPatchedVersion {identifier}
            severity
          }
        }
      }
    }
  }
}

"""
# Insert repo and org info into the query.
query = query.replace('MYREPO', args.repository )
query = query.replace('MYORG', args.owner )

result = run_query(query) # Execute the query
print(json.dumps(result))
#print result
#remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
#print("Remaining rate limit - {}".format(remaining_rate_limit))