#create directories
import os, shutil
def makeDir(dir):
    try:
        root = os.path.abspath(os.path.dirname(__file__))
        dir = os.path.join(root, dir)
        os.mkdir(dir)
    except OSError as exc:
        print("error making "+ dir + "-"+exc.strerror)

def clear_folder_files(dir):
    root = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(root, dir)

    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

RECORDIO_TRAIN_FILE = '../recordIO_dir/Train.rec'
RECORDIO_VAL_FILE ='../recordIO_dir/Val.rec'
RECORDIO_TEST_FILE ='../recordIO_dir/Test.rec'

domain = 'https://openi.nlm.nih.gov'
json_data_file = 'data_new.json'

images_directory = "../images_all"

record_IO_directory = "../recordIO_dir"

clear_subdirs = True   #clear the following subdirs before copying
mxnet_images_train_dir = "../data/train"
mxnet_images_train_nodule_dir = mxnet_images_train_dir + "/nodule"
mxnet_images_train_normal_dir = mxnet_images_train_dir + "/normal"
mxnet_images_val_dir = "../data/valid"
mxnet_images_val_nodule_dir = mxnet_images_val_dir + "/nodule"
mxnet_images_val_normal_dir = mxnet_images_val_dir + "/normal"
mxnet_images_test_dir = "../data/test"
mxnet_images_test_nodule_dir = mxnet_images_test_dir + "/nodule"
mxnet_images_test_normal_dir = mxnet_images_test_dir + "/normal"

number_pages = 75

#test with just 20 images, much-much faster
test_run = True
test_images = 200   #default, may also test with at most number nodule images(nodule and normal)


trainpercent = .7
valpercent = .15
testpercent = .15

#if datasets unbalanced (numb_nodule<<numb_normal) then make copies of nodule dataset
#until numb_nodule==numb_normal
force_balance = True