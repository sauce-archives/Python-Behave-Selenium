run_all_in_parallel:
	make -j chrome_case firefox_case ie_case

chrome_case:
	browserName=chrome platform="Windows 10" version="latest" behave-parallel/bin/behave --processes 12 --parallel-element scenario

firefox_case:
	browserName=firefox platform="Windows 10" version="latest" behave-parallel/bin/behave --processes 12 --parallel-element scenario

ie_case:
	browserName="internet explorer" platform="Windows 10" version="latest" behave-parallel/bin/behave --processes 12 --parallel-element scenario