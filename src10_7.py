"""
Сервис избранного
с. 287
"""
import functools
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Pool

from src10_4 import DB_KEY, create_database_pool, destroy_database_pool
from util import get_secret

routes = web.RouteTableDef()


@routes.get('/products')
async def products(request: Request) -> Response:
    db: Pool = request.app[DB_KEY]
    products_query = 'SELECT product_id, product_name FROM product'
    result = await db.fetch(products_query)
    return web.json_response([dict(record) for record in result])


app = web.Application()
app.on_startup.append(functools.partial(
    create_database_pool,
    host='127.0.0.1',
    port=5432,
    user='postgres',
    password=get_secret('POSTGRES_PASSWORD'),
    database='products',
))
app.on_cleanup.append(destroy_database_pool)
app.add_routes(routes)
web.run_app(app, port=8000)
