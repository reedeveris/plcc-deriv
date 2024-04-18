#!/usr/bin/env bats

load '../../relocate_to_temp.bash'

@test "PLCC compiles OBJ in Python." {
  relocate_to_temp

  cd OBJ
  run plccmk grammar

  # Print stdout and stderr for debugging.
  echo "OUTPUT: $output"
  echo "ERROR: $error"

  # Assert success.
  [ "$status" -eq 0 ]
}
