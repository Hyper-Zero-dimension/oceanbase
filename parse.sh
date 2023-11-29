bash build.sh release --init --make -j4
rm -rf ../obcluster/bin/observer
cp build_release/src/observer/observer ../obcluster/bin/observer