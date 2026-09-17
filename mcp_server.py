import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Airbnb Data API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "airbnb_search",
    "method": "POST",
    "path": "/airbnb/search",
    "description": "V1 Airbnb Search"
  },
  {
    "name": "airbnb_details",
    "method": "POST",
    "path": "/airbnb/details",
    "description": "V1 Airbnb Details"
  },
  {
    "name": "airbnb_calendar",
    "method": "POST",
    "path": "/airbnb/calendar",
    "description": "V1 Airbnb Calendar"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
