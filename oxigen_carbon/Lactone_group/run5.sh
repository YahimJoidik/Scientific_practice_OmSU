
# outputs calculation directory into htop:
PWD=`pwd`
LAST_PART=${PWD/"/home/netusers/joidikefim/"/}

# execute 6 version of VASP compiled by "GCC" on lab:
nohup mpirun -np 4 vasp6_std $LAST_PART > log.txt 2> error.err < /dev/null &

# execute 6 version of VASP compiled by "intel oneApi" on lab:
#nohup mpiexec -np 4 vasp6_std_intel $LAST_PART > log.txt 2> error.err < /dev/null &

# execute 6 version of VASP compiled by "GCC+AOCL" on think:
#nohup mpirun -np 4 vasp6_std $LAST_PART > log.txt 2> error.err < /dev/null &

# execute 6 version of VASP compiled by intel "oneApi" on dl:
#nohup mpiexec -np 4 vasp6_std_intel $LAST_PART > log.txt 2> error.err < /dev/null &

# use "std" for standart (collinear) VASP
# use "ncl" for noncollinear VASP
