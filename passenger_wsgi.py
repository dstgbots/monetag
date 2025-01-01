import sys, os
INTERP = os.path.join(os.getcwd(), 'venv', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

from app import create_app
application = create_app()

