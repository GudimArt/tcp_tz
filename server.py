import asyncio, json  

from  logger import init_logger

from settings_server import HOST, PORT


async def calculate_expression (math_expression) -> int:
    try:
        result = eval(math_expression)
        logger_server.info(f'Calculation result: {result}')
        return result
    except Exception as e:
        logger_server.warning(f"Calculation failed, User entered: {math_expression}. \n {e}")
        return None

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    data = await reader.read(255)
    logger_server.info(f"Received: {data} from {addr}")
    math_expression = json.loads(data.decode())
    logger_server.info(f"Decoded data: {math_expression}")
    response = await calculate_expression(math_expression) 
    if response == None:
        response = "Error, check your input"
    else:
        response = str(response)
    response_json = json.dumps(response).encode()
    logger_server.info(f"Encode response: {response_json}")
    writer.write(response_json)
    await writer.drain()
    logger_server.info(f"Sending: {response_json}")
    writer.close()
    logger_server.info("Connection closed")


async def run_server():
    server = await asyncio.start_server(client_connected_cb = handle_client, host = HOST, port = PORT)
    logger_server.info(f'Serving on ({HOST}:{PORT})')
    async with server:
        await server.serve_forever()

logger_server = init_logger('server')
asyncio.run(run_server())