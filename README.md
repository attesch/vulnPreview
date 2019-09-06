# GitHub Preview - GraphQL API v4 Repository Vulnerability Alerts

## Running this from locally installed Python

```shell
pip install -r requirements.txt
python test-github.py --owner attesch --repository vulnPreview --token <putyourtokenherewhenrunning>
```

## running from a python docker image

You must have Docker installed and running on your local machine

```shell
## Start the python container
docker run -it --rm -v $(pwd):/vulnPreview --workdir /vulnPreview python /bin/bash
```

## Building and running your own docker image

```shell
docker build --tag vulnpreview:1.0 .
docker run -it --rm vulnpreview:1.0 test-github.py --owner attesch --repository vulnPreview --token <putyourtokenherewhenrunning>
```

## Summary Branch

The summary branch contains updates to the test-github.py script that outputs a header line and a values line that could be used in a CSV file.  The thought is that this data in whole or part could be put on a dashboard.

```shell
python test-github.py --owner attesch --repository cezerin --token <yourgittokenhere>
Organization,Repository,LOW,MED,HIGH,CRITICAL
attesch,cezerin,1,0,3,6

python test-github.py --owner attesch --repository cezerin --token <yourgittokenhere> > results.csv

```

## Output from Master Branch 

I ran this from a docker container against one of my personal repos that I forked from Cezerin a NodeJs ecommerce app.

```shell
root@d878cf63fb68:/gitgraph# python test-github.py --owner attesch --repository cezerin --token <REMOVED>
{"data": {"repository": {"name": "cezerin", "vulnerabilityAlerts": {"totalCount": 3, "edges": [{"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NA==", "packageName": "slug", "securityVulnerability": {"package": {"name": "slug"}, "firstPatchedVersion": null, "severity": "HIGH"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NQ==", "packageName": "lodash", "securityVulnerability": {"package": {"name": "lodash"}, "firstPatchedVersion": {"identifier": "4.17.11"}, "severity": "LOW"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MzAyNTQ2OA==", "packageName": "tar", "securityVulnerability": {"package": {"name": "tar"}, "firstPatchedVersion": {"identifier": "2.2.2"}, "severity": "HIGH"}}}]}}}}
```