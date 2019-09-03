test = {
  'name': 'Question 1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(aa_san_dests_with_lat_diff,Table)
          True
          >>> 'Dest' in aa_san_dests_with_lat_diff.labels
          True
          >>> 'latitude_difference' in aa_san_dests_with_lat_diff.labels
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}