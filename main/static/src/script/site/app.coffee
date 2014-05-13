$ ->
  init_common()

$ -> ($ 'html.welcome').each ->
  LOG('init welcome')

$ -> ($ 'html.profile').each ->
  init_profile()

$ -> ($ 'html.signin').each ->
  init_signin()

$ -> ($ 'html.feedback').each ->

$ -> ($ 'html.user-list').each ->
  init_user_list()

$ -> ($ 'html.user-merge').each ->
  init_user_merge()

$ -> ($ 'html.admin-config').each ->
  init_admin_config()

$ -> ($ 'html.gae').each ->
  location.href = 'https://plus.google.com/events/c5du3ag4pgq1scg21573s1ppom0'
