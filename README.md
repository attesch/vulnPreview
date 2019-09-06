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

The current version of the script does not parse the results of the script.  The results are returned as json, and I use Windows Powershell to look at the results.

```powershell
$results = docker run -it --rm vulnpreview:1.0 test-github.py --owner myorg --repository myrepository --token <putyourtokenherewhenrunning> | convertfrom-json

$results.data.repository.vulnerabilityAlerts.edges.node.securityVulnerability

severity firstPatchedVersion   package
-------- -------------------   -------
HIGH                           @{name=slug}
LOW      @{identifier=4.17.11} @{name=lodash}
MODERATE @{identifier=1.0.12}  @{name=fstream}
HIGH     @{identifier=3.13.1}  @{name=js-yaml}
MODERATE @{identifier=3.13.0}  @{name=js-yaml}
MODERATE @{identifier=2.3.1}   @{name=braces}
MODERATE @{identifier=3.1.0}   @{name=esm}
MODERATE @{identifier=4.0.0}   @{name=mem}
CRITICAL @{identifier=4.6.2}   @{name=lodash.merge}
CRITICAL @{identifier=4.17.14} @{name=lodash-es}
CRITICAL @{identifier=4.6.2}   @{name=lodash.mergewith}
CRITICAL @{identifier=4.5.0}   @{name=lodash.template}
CRITICAL @{identifier=4.17.13} @{name=lodash}
HIGH     @{identifier=4.0.14}  @{name=handlebars}
MODERATE @{identifier=4.17.11} @{name=lodash}
CRITICAL @{identifier=1.4.1}   @{name=eslint-utils}

$results.data.repository.vulnerabilityAlerts.edges.node.securityVulnerability |Group-Object severity |select count,name

Count Name
----- ----
    3 HIGH
    1 LOW
    6 MODERATE
    6 CRITICAL

```

## Output

I ran this from a docker container against one of my personal repos that I forked from Cezerin a NodeJs ecommerce app.

```shell
root@d878cf63fb68:/gitgraph# python test-github.py --owner attesch --repository cezerin --token <REMOVED>
{"data": {"repository": {"name": "cezerin", "vulnerabilityAlerts": {"totalCount": 3, "edges": [{"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NA==", "packageName": "slug", "securityVulnerability": {"package": {"name": "slug"}, "firstPatchedVersion": null, "severity": "HIGH"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NQ==", "packageName": "lodash", "securityVulnerability": {"package": {"name": "lodash"}, "firstPatchedVersion": {"identifier": "4.17.11"}, "severity": "LOW"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MzAyNTQ2OA==", "packageName": "tar", "securityVulnerability": {"package": {"name": "tar"}, "firstPatchedVersion": {"identifier": "2.2.2"}, "severity": "HIGH"}}}]}}}}
```