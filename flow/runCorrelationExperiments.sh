#!/usr/bin/env bash

function initialize_flow_files {
  local mpl_pause_step=$1

  cd logs/${design}/
  mkdir "$mpl_pause_step"
  cp -R base/* "$mpl_pause_step"/
  cd -

  cd objects/${design}/
  mkdir "$mpl_pause_step"
  cp -R base/* "$mpl_pause_step"/
  cd -

  cd reports/${design}/
  mkdir "$mpl_pause_step"
  cp -R base/* "$mpl_pause_step"/
  cd -

  cd results/${design}/
  mkdir "$mpl_pause_step"
  cp -R base/* "$mpl_pause_step"/
  cd -
}

function run_from_mpl {
  local mpl_pause_step=$1
  export RTLMP_PAUSE_AT_STEP="$mpl_pause_step"
  export FLOW_VARIANT="$mpl_pause_step"

  initialize_flow_files $mpl_pause_step

  make do-2_2_floorplan_macro do-2_3_floorplan_tapcell do-2_4_floorplan_pdn do-2_floorplan do-2_floorplan.sdc do-place
}

design="gf12/ariane"
export DESIGN_CONFIG=./designs/${design}/config.mk
export RTLMP_DATA_FLOW_DRIVEN=0
#export RTLMP_TIMING_DRIVEN=1

make synth
make do-2_1_floorplan

for ((mpl_pause_step = 50; mpl_pause_step <= 500; mpl_pause_step = mpl_pause_step + 30)); do
    run_from_mpl $mpl_pause_step
done
