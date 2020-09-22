pwd
module load intel/cluster/2018
ulimit -s unlimited 
export post_bin_path=/home/dhp/public/postproc/dev
export PATH=$post_bin_path:$PATH
ee $*
