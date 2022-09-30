import site

sites = site.getsitepackages() + [site.getusersitepackages()]
print('\n'.join(sites))
