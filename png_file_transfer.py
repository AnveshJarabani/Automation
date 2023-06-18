import re, glob, os
import warnings, shutil
import multiprocessing as mp

# lst=[r'{}'.format(i) for i in pths.keys()]
current_favs = r"C:\Users\anves\OneDrive\Desktop\Sweety Iphone\Favs"
icloud = r"C:\Users\anves\OneDrive\Desktop\Sweety Iphone\Icloud pics"
new_favs = r"C:\Users\anves\OneDrive\Desktop\Sweety Iphone\fav1"
fav_lst = glob.glob(current_favs + "/*")
icloud_lst = glob.glob(icloud + "/*")
fav_files = [os.path.basename(i) for i in fav_lst]
icloud_files = [os.path.basename(i) for i in icloud_lst]
new_favs = r"C:\Users\anves\OneDrive\Desktop\Sweety Iphone\fav1"
icloud_files_names = [i.split(".")[0] for i in icloud_files]
fav_files_names = [i.split(".")[0] for i in fav_files]
icloud_favs_names = [i for i in icloud_files_names if i in fav_files_names]
for i in icloud_favs_names:
    for icl_path in icloud_lst:
        if i in icl_path:
            shutil.copy(icl_path, new_favs)
# lst = [r"{}".format(path) for path in lst]
