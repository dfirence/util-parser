import os


def inspect_file(fpath):
  fpath = os.path.abspath(fpath)

  if os.path.exists(fpath)            \
    and os.path.isfile(fpath)         \
    and (os.path.getsize(fpath) > 0):
    return os.stat(fpath)
    
  else:
    return False