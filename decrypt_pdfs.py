import os
from subprocess import call

# TODO: Script to dl all pdf files

for root, dirs, files in os.walk("."):
    for file in files:

        # skip already decrypted
        if file.startswith('dec_'):
            continue

        # skip none pdfs
        if not file.endswith('.pdf'):
            continue


        # found a file to decrypt
        print('found file: ', file)
        print(os.path.join(root, file))

        new_name = 'dec_{}'.format(file)

        call('qpdf --password='' --decrypt %s %s' %(os.path.join(root, file), os.path.join(root, new_name)), shell=True)

        #TODO: remove none decrypted .pdf
