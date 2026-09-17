# Airbnb Data API

> Airbnb search, listing details, and calendar availability as clean structured data.

Part of the **DataLeads** API suite (Travel category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/airbnb/search` | V1 Airbnb Search |
| POST | `/airbnb/details` | V1 Airbnb Details |
| POST | `/airbnb/calendar` | V1 Airbnb Calendar |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/airbnb/search \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "location": "Austin, TX"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/airbnb-data`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/airbnb-data-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
