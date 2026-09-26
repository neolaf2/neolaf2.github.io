#!/usr/bin/env python3
"""Retrieve canonical pages into a review-only staging directory; never overwrite content."""
from pathlib import Path
from urllib.request import Request,urlopen
from html.parser import HTMLParser
from datetime import datetime,timezone
import json,hashlib,argparse
class Extract(HTMLParser):
 def __init__(self): super().__init__();self.rows=[];self.row=None;self.cell=None;self.text=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.skip+=1
  if tag=='tr':self.row=[]
  if tag in ('td','th'):self.cell=[]
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
  if tag in ('td','th') and self.cell is not None:
   if self.row is not None:self.row.append(' '.join(' '.join(self.cell).split()))
   self.cell=None
  if tag=='tr' and self.row is not None:
   if self.row:self.rows.append(self.row)
   self.row=None
 def handle_data(self,data):
  if not self.skip and data.strip():self.text.append(data.strip())
  if self.cell is not None:self.cell.append(data)
p=argparse.ArgumentParser();p.add_argument('--output',default='/tmp/aisc-ieee-review');args=p.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
manifest=[]
for name,path in [('committee',''),('standards','standards/'),('projects','active-pars/'),('participation','how-to-participate/')]:
 url='https://sagroups.ieee.org/ai-sc/'+path;entry={'source':url,'retrieved_at':datetime.now(timezone.utc).isoformat(),'publication':'Review required'}
 try:
  with urlopen(Request(url,headers={'User-Agent':'AISC-community-source-review/1.0'}),timeout=25) as r:raw=r.read()
  parser=Extract();parser.feed(raw.decode('utf-8',errors='replace'))
  text=' '.join(parser.text)
  if len(text)<300 or any(s in text.lower() for s in ['verify you are human','checking your browser','access denied']):raise ValueError('Source returned no usable committee content')
  entry.update(status='retrieved',sha256=hashlib.sha256(raw).hexdigest(),rows=parser.rows,text=text)
  (out/(name+'.html')).write_bytes(raw)
 except Exception as e:entry.update(status='unavailable',error=str(e))
 manifest.append(entry)
(out/'candidates.json').write_text(json.dumps(manifest,indent=2))
print('Review candidates saved to',out,'; no published records modified.')
