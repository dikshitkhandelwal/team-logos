import  boto3

dc = {}

conn = boto3.client("s3")

for key in conn.list_objects(Bucket = "sports-team-logos")["Contents"]:
    first = key["Key"]
    sports = first.split("/")[0]
    team = first.split("/")[1].split(".png")[0]
    if sports not in dc.keys():
        dc[sports] = [team]
    else:
        dc[sports].append(team)
    
print(dc)