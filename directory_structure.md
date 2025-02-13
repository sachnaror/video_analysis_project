├── video_analysis_project/
│   ├── dump.rdb
│   ├── requirements.txt
│   ├── yolov8n.pt
│   ├── db.sqlite3
│   ├── README.md
│   ├── database.env
│   ├── docker-compose.yml
│   ├── manage.py
│   ├── celery_tasks.py
│   ├── app/
│   │   ├── video_processing.py
│   │   ├── tasks.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── chat_processor.py
│   │   ├── consumers.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── routing.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config/
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── Dockerfile/
│   ├── staticfiles/
│   │   ├── styles.css
│   │   └── script.js
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   │   ├── widgets.css
│   │   │   │   ├── dark_mode.css
│   │   │   │   ├── login.css
│   │   │   │   ├── dashboard.css
│   │   │   │   ├── nav_sidebar.css
│   │   │   │   ├── responsive.css
│   │   │   │   ├── autocomplete.css
│   │   │   │   ├── responsive_rtl.css
│   │   │   │   ├── forms.css
│   │   │   │   ├── unusable_password_field.css
│   │   │   │   ├── rtl.css
│   │   │   │   ├── base.css
│   │   │   │   └── changelists.css
│   │   │   │   ├── vendor/
│   │   │   │   │   ├── select2/
│   │   │   │   │   │   ├── select2.min.css
│   │   │   │   │   │   ├── LICENSE-SELECT2.md
│   │   │   │   │   │   └── select2.css
│   │   │   ├── js/
│   │   │   │   ├── urlify.js
│   │   │   │   ├── core.js
│   │   │   │   ├── actions.js
│   │   │   │   ├── prepopulate.js
│   │   │   │   ├── cancel.js
│   │   │   │   ├── theme.js
│   │   │   │   ├── nav_sidebar.js
│   │   │   │   ├── autocomplete.js
│   │   │   │   ├── inlines.js
│   │   │   │   ├── change_form.js
│   │   │   │   ├── filters.js
│   │   │   │   ├── SelectFilter2.js
│   │   │   │   ├── jquery.init.js
│   │   │   │   ├── popup_response.js
│   │   │   │   ├── SelectBox.js
│   │   │   │   ├── calendar.js
│   │   │   │   ├── unusable_password_field.js
│   │   │   │   └── prepopulate_init.js
│   │   │   │   ├── admin/
│   │   │   │   │   ├── RelatedObjectLookups.js
│   │   │   │   │   └── DateTimeShortcuts.js
│   │   │   │   ├── vendor/
│   │   │   │   │   ├── jquery/
│   │   │   │   │   │   ├── jquery.min.js
│   │   │   │   │   │   ├── LICENSE.txt
│   │   │   │   │   │   └── jquery.js
│   │   │   │   │   ├── xregexp/
│   │   │   │   │   │   ├── xregexp.min.js
│   │   │   │   │   │   ├── xregexp.js
│   │   │   │   │   │   └── LICENSE.txt
│   │   │   │   │   ├── select2/
│   │   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   │   ├── select2.full.min.js
│   │   │   │   │   │   └── select2.full.js
│   │   │   │   │   │   ├── i18n/
│   │   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   │   ├── hsb.js
│   │   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   │   ├── dsb.js
│   │   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   │   ├── hy.js
│   │   │   │   │   │   │   ├── sr-Cyrl.js
│   │   │   │   │   │   │   ├── ne.js
│   │   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   │   ├── az.js
│   │   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   │   ├── zh-CN.js
│   │   │   │   │   │   │   ├── zh-TW.js
│   │   │   │   │   │   │   ├── pt-BR.js
│   │   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   │   ├── tk.js
│   │   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   │   ├── ps.js
│   │   │   │   │   │   │   └── tr.js
│   │   │   ├── img/
│   │   │   │   ├── search.svg
│   │   │   │   ├── icon-calendar.svg
│   │   │   │   ├── icon-clock.svg
│   │   │   │   ├── icon-hidelink.svg
│   │   │   │   ├── icon-no.svg
│   │   │   │   ├── tooltag-add.svg
│   │   │   │   ├── inline-delete.svg
│   │   │   │   ├── LICENSE
│   │   │   │   ├── icon-changelink.svg
│   │   │   │   ├── icon-unknown.svg
│   │   │   │   ├── sorting-icons.svg
│   │   │   │   ├── icon-viewlink.svg
│   │   │   │   ├── icon-yes.svg
│   │   │   │   ├── icon-addlink.svg
│   │   │   │   ├── icon-unknown-alt.svg
│   │   │   │   ├── icon-deletelink.svg
│   │   │   │   ├── README.txt
│   │   │   │   ├── selector-icons.svg
│   │   │   │   ├── calendar-icons.svg
│   │   │   │   ├── tooltag-arrowright.svg
│   │   │   │   └── icon-alert.svg
│   │   │   │   ├── gis/
│   │   │   │   │   ├── move_vertex_on.svg
│   │   │   │   │   └── move_vertex_off.svg
│   │   ├── rest_framework/
│   │   │   ├── css/
│   │   │   │   ├── bootstrap.min.css
│   │   │   │   ├── bootstrap.min.css.map
│   │   │   │   ├── bootstrap-theme.min.css.map
│   │   │   │   ├── prettify.css
│   │   │   │   ├── default.css
│   │   │   │   ├── font-awesome-4.0.3.css
│   │   │   │   ├── bootstrap-tweaks.css
│   │   │   │   └── bootstrap-theme.min.css
│   │   │   ├── js/
│   │   │   │   ├── load-ajax-form.js
│   │   │   │   ├── ajax-form.js
│   │   │   │   ├── prettify-min.js
│   │   │   │   ├── csrf.js
│   │   │   │   ├── bootstrap.min.js
│   │   │   │   ├── default.js
│   │   │   │   ├── coreapi-0.1.1.js
│   │   │   │   └── jquery-3.7.1.min.js
│   │   │   ├── docs/
│   │   │   │   ├── css/
│   │   │   │   │   ├── highlight.css
│   │   │   │   │   ├── base.css
│   │   │   │   │   └── jquery.json-view.min.css
│   │   │   │   ├── js/
│   │   │   │   │   ├── highlight.pack.js
│   │   │   │   │   ├── api.js
│   │   │   │   │   └── jquery.json-view.min.js
│   │   │   │   ├── img/
│   │   │   │   │   ├── favicon.ico
│   │   │   │   │   └── grid.png
│   │   │   ├── img/
│   │   │   │   ├── grid.png
│   │   │   │   ├── glyphicons-halflings.png
│   │   │   │   └── glyphicons-halflings-white.png
│   │   │   ├── fonts/
│   │   │   │   ├── fontawesome-webfont.svg
│   │   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   │   ├── glyphicons-halflings-regular.woff2
│   │   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   │   ├── fontawesome-webfont.ttf
│   │   │   │   ├── fontawesome-webfont.woff
│   │   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   │   └── fontawesome-webfont.eot
│   ├── static/
│   │   ├── styles.css
│   │   └── script.js
│   ├── templates/
│   │   ├── index.html
│   │   └── reports.html
│   ├── media/
│   │   └── progress.json
│   │   ├── transcripts/
│   │   │   ├── Screen Recording 2025-02-08 at 9.49.34PM.mov_transcript.txt
│   │   │   └── Screen Recording 2025-02-13 at 2.04.42AM.mov_transcript.txt
│   │   ├── analysis/
│   │   │   ├── Screen Recording 2025-02-13 at 2.04.42AM.mov_analysis.txt
│   │   │   └── Screen Recording 2025-02-08 at 9.49.34PM.mov_analysis.txt
│   │   └── frames/
│   │   ├── uploads/
│   │   │   ├── Employee Group Mediclaim Insurance Policy-NEW.pdf
│   │   │   ├── Screen Recording 2025-02-08 at 9.49.34PM.mov
│   │   │   └── Screen Recording 2025-02-13 at 2.04.42AM.mov
│   │   └── chunks/
│   │   └── audio/
