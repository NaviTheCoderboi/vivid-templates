from vivid.app import Response


async def load():
    return Response(200, [], {"user": "vivid"})