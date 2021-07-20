#!/user/bin/env python
# -*- coding: utf8 -*-

try:
    from configuration.conf_fastapi import create_app

    app = create_app(debug=False)

except Exception as e:
    import sys
    import traceback

    traceback.print_exc()
    print("*"*80 + "nErrot: " + str(e))
    sys.exit(-1)

if __name__ == '__main__':

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000, log_level='info')

    # app.run(host='0.0.0.0', post=5000, debug=True)
