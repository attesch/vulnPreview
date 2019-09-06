# An example to get the remaining rate limit using the Github GraphQL API.

import requests
import simplejson as json
import argparse

parser = argparse.ArgumentParser(description="Beta GraphQL query for Github Vulnerabilities.")
parser.add_argument('--owner', help='owner or organization name where repository is located')
parser.add_argument('--repository', help='github repository to check for known vulnerabilities')
parser.add_argument('--token', help='github token that can query repo')
parser.add_argument('--result', help='produces [summary] or [raw] output')
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
vulncount = result["data"]["repository"]["vulnerabilityAlerts"]["totalCount"]
#print("\n")
#print("Total vulnerabilities Found : {0}".format(vulncount))
#print("\n")
#print countmessage
#.data.repository.vulnerabilityAlerts.edges.node.securityVulnerability
#out = result["data"]["repository"]["vulnerabilityAlerts"]["edges"]["node"]["securityVulnerability"]["severity"])

if args.result == "summary":
  low=0
  med=0
  high=0
  crit=0
  for edge in result["data"]["repository"]["vulnerabilityAlerts"]["edges"]:
    sev = edge["node"]["securityVulnerability"]["severity"]
    if sev == "LOW":
      low=low+1
    if sev == "MEDIUM":
      med=med+1
    if sev == "HIGH":
      high=high+1
    if sev == "CRITICAL":
      crit=crit+1

  dict_result = {"Organization": args.owner, "Repository": args.repository, "Low": low, "Medium": med, "High": high,"Critical": crit}
  print(dict_result)

if args.result == "raw":
  print("Total vulnerabilities Found : {0}".format(vulncount))
  print(json.dumps(result)) 

## This output can be written to a file as a CSV. The file could be appended to and could include a date/time stamp for tracking vlaues over time.
#print("Organization,Repository,LOW,MED,HIGH,CRITICAL")
#print("{0},{1},{2},{3},{4},{5}".format(args.owner,args.repository,low, med, high, crit))
#print(json.dumps(out))
#print(json.dumps(result))
#print(json.dumps(result["data"]["repository"]["vulnerabilityAlerts"]["edges"]))
#print result
#remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
#print("Remaining rate limit - {}".format(remaining_rate_limit))