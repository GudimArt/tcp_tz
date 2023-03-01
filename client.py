import asyncio, json

from  logger import init_logger
  
from settings_server import HOST, PORT


async def tcp_echo_client(math_expression):
    reader, writer = await asyncio.open_connection(host=HOST, port=PORT)
    logger_client.info(f"Connected to {HOST}:{PORT}")
    math_expression_json = json.dumps(math_expression).encode()
    logger_client.info(f"Encoded math expression: {math_expression_json}")
    writer.write(math_expression_json)
    logger_client.info(f"Sending: {math_expression}")
    result = await reader.read(100)
    logger_client.info(f"Received: {result}")
    result = json.loads(result.decode())
    logger_client.info(f"Decoded result: {result}")
    writer.close()
    logger_client.info("Connection closed")

logger_client = init_logger('client')
asyncio.run(tcp_echo_client(input()))