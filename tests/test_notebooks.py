import datetime, os, re, subprocess, sys, argparse, time, unittest


ignoreFlag=True   # change to False if not to ignore  



def test_notebook(path):
    """
    Tests a notebook in a subprocess, exists if it doesn't finish.
    """
    import nbconvert
    print('Running ' + path + ' ... ', end='')
    sys.stdout.flush()

    # Load notebook, convert to python
    e = nbconvert.exporters.PythonExporter()
    code, __ = e.from_filename(path)

    # Remove coding statement, if present
    ipylines = ['ipython', 'show(']
    code = '\n'.join([x for x in code.splitlines() if not 'ipython' in x])
    for x in code.splitlines():
        if not any(s in ipylines for s in x):
            code += '\n'.join([x])
    # print(code)

    # Tell matplotlib not to produce any figures
    env = os.environ.copy()
    env['MPLBACKEND'] = 'Template'

    # Run in subprocess
    start = time.time()
    cmd = [sys.executable, '-c', code]
    try:
        p = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env
        )
        stdout, stderr = p.communicate()
        # TODO: Use p.communicate(timeout=3600) if Python3 only
        if p.returncode != 0:
            # Show failing code, output and errors before returning
            print('ERROR')
            # print('-- script ' + '-' * (79 - 10))
            # for i, line in enumerate(code.splitlines()):
            #     j = str(1 + i)
            #     print(j + ' ' * (5 - len(j)) + line)
            print('-- stdout ' + '-' * (79 - 10))
            print(stdout)
            print('-- stderr ' + '-' * (79 - 10))
            print(stderr)
            print('-' * 79)
            return False
    except KeyboardInterrupt:
        p.terminate()
        stop = time.time()
        print('ABORTED after', round(stop-start,4), "s")
        sys.exit(1)

    # Successfully run
    stop = time.time()
    print('ok. Run took ', round(stop-start,4), "s")
    return True


def export_notebook(ipath, opath):
    """
    Exports the notebook at `ipath` to a python file at `opath`.
    """
    import nbconvert
    from traitlets.config import Config

    # Create nbconvert configuration to ignore text cells
    c = Config()
    c.TemplateExporter.exclude_markdown = True

    # Load notebook, convert to python
    e = nbconvert.exporters.PythonExporter(config=c)
    code, __ = e.from_filename(ipath)

    # Remove "In [1]:" comments
    r = re.compile(r'(\s*)# In\[([^]]*)\]:(\s)*')
    code = r.sub('\n\n', code)

    # Store as executable script file
    with open(opath, 'w') as f:
        f.write('#!/usr/bin/env python')
        f.write(code)
    os.chmod(opath, 0o775)


cwd0 =os.getcwd()
os.chdir('../examples/')
cwd =os.getcwd()

path1 = cwd+'/ex01-unboundedFlow.ipynb'   
path2 = cwd+'/ex02-flowPlaneSurface.ipynb'
path5 = cwd+'/ex03-crystalNucleation.ipynb' 
path3 = cwd+'/ex05-phoreticField.ipynb'
path4 = cwd+'/ex08-holographicTrap.ipynb' 
test_notebook(path1)
test_notebook(path2)
test_notebook(path3)
test_notebook(path4)
test_notebook(path5)
