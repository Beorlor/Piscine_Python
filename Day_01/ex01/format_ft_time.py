    from datetime import datetime

    # Temps écoulé depuis le 1er janvier 1970
    timestamp = datetime.now().timestamp()

    print(f"Seconds since January 1, 1970: {timestamp:.4f} or {timestamp:.2e} in scientific notation")
    print(datetime.now().strftime("%b %d %Y"))
