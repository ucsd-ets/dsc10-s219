test = {
  'name': 'Question 4_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(predictions_array) == 4
          True
          >>> set(np.unique(predictions_array)) == set(['Yes','No'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
