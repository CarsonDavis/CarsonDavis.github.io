.PHONY: build deploy setup-trigger test-compressor test-lqip clean

build:
	sam build

deploy:
	sam deploy --guided

deploy-ci:
	sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

setup-trigger:
	bash setup_s3_trigger.sh

test-compressor:
	sam local invoke ImageCompressorFunction -e events/compressor_test.json

test-lqip:
	sam local invoke LqipGeneratorFunction -e events/lqip_test.json

clean:
	rm -rf .aws-sam
