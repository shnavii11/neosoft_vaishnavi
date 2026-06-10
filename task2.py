• def flatten_typed(data):
      groups = {
          "integers": set(),
          "floats": set(),
          "strings": set(),
          "booleans": set()
      }

      def flatten(items):
          for value in items:
              # process nested lists using recursion
              if isinstance(value, list):
                  flatten(value)

              # check bool before int because bool is a subclass of int
              #True and False would enter the integer bucket before Python reached the Boolean check.
             elif isinstance(value, bool):
                  groups["booleans"].add(value)

              elif isinstance(value, int):
                  groups["integers"].add(value)

              elif isinstance(value, float):
                  groups["floats"].add(value)

              elif isinstance(value, str):
                  groups["strings"].add(value)

              # raise an error for unsupported types
              else:
                  raise TypeError(
                      f"Unsupported type: {type(value).__name__}"
                  )

      # check if the main input is a list
      if not isinstance(data, list):
          raise TypeError(
              f"Unsupported type: {type(data).__name__}"
          )

      flatten(data)

      # convert sets to sorted lists and remove empty groups
      return {
          name: sorted(values)
          for name, values in groups.items()
          if values
      }


  # test 1: integers only
  test1 = [1, [2, [3, 2]], 1, [4]]
  print("test 1:", flatten_typed(test1))


  # test 2: mixed int, float, and str
  test2 = [3, ["apple", 1.5], ["apple", [2, 1.5, "banana"]]]
  print("test 2:", flatten_typed(test2))


  # test 3: bool and int separation
  test3 = [True, 1, False, [True, 0, [2, False]]]
  print("test 3:", flatten_typed(test3))


  # test 4: unsupported dictionary
  test4 = [1, [2, {"key": "val"}]]

  try:
      print("test 4:", flatten_typed(test4))
  except TypeError as error:
      print("test 4 error:", error)
