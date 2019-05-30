# vulnPreview

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

After the container starts follow the python code snippet above to run.

## Output

I ran this from a docker container against one of my personal repos that I forked from Cezerin a NodeJs ecommerce app.

```shell
root@d878cf63fb68:/gitgraph# python test-github.py --owner attesch --repository cezerin --token <REMOVED>
{"data": {"repository": {"name": "cezerin", "vulnerabilityAlerts": {"totalCount": 3, "edges": [{"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NA==", "packageName": "slug", "securityVulnerability": {"package": {"name": "slug"}, "firstPatchedVersion": null, "severity": "HIGH"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MTE4NTA1NQ==", "packageName": "lodash", "securityVulnerability": {"package": {"name": "lodash"}, "firstPatchedVersion": {"identifier": "4.17.11"}, "severity": "LOW"}}}, {"node": {"id": "MDI4OlJlcG9zaXRvcnlWdWxuZXJhYmlsaXR5QWxlcnQ5MzAyNTQ2OA==", "packageName": "tar", "securityVulnerability": {"package": {"name": "tar"}, "firstPatchedVersion": {"identifier": "2.2.2"}, "severity": "HIGH"}}}]}}}}
```

