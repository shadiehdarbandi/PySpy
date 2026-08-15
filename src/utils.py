async def Notifall(msg: dict, users):
    for ws in users:
        try:
            if ws is None:
                print(f'Notifall skipped: ws is None for msg={msg}')
                continue
            await ws.send_json(msg)
            print(f'Notifall sent successfully: {msg}')
        except Exception as err:
            print(f'Notifall FAILED for msg={msg} - error: {err}')
