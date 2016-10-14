$ ->
  init_common()

$ -> $('html.auth').each ->
  init_auth()

$ -> $('html.user-list').each ->
  init_user_list()

$ -> $('html.user-merge').each ->
  init_user_merge()

$ -> ($ 'html.gae').each ->
  location.href = 'https://plus.google.com/events/c5du3ag4pgq1scg21573s1ppom0'
