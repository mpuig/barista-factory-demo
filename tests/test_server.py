import io,json,os,tempfile,unittest
from pathlib import Path
class ServerTest(unittest.TestCase):
 def test_health_and_events(self):
  with tempfile.TemporaryDirectory() as d:
   os.environ['BARISTA_DEMO_DB']=str(Path(d)/'events.sqlite3')
   import importlib,app.server as server; importlib.reload(server)
   def call(path,method='GET',body=b''):
    status=[]
    result=server.application({'PATH_INFO':path,'REQUEST_METHOD':method,'CONTENT_LENGTH':str(len(body)),'wsgi.input':io.BytesIO(body)},lambda value,_:status.append(value))
    return status[0],json.loads(b''.join(result))
   self.assertEqual(call('/api/health')[0],'200 OK')
   self.assertEqual(call('/api/events','POST',b'{"revision":"abc","status":"healthy"}')[0],'201 Created')
   self.assertEqual(len(call('/api/events')[1]),1)
