run_all_in_parallel:
	make -j xp_chrome_41 xp_firefox_33 Windows7_ie_10

xp_chrome_41:
	browserName=chrome platform=XP version=41 behave-parallel/bin/behave --processes 12 --parallel-element scenario

xp_firefox_33:
	browserName=firefox platform=XP version=33 behave-parallel/bin/behave --processes 12 --parallel-element scenario

Windows7_ie_10:
	browserName="internet explorer" platform="Windows 7" version=10 behave-parallel/bin/behave --processes 12 --parallel-element scenario