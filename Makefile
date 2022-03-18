create:
	kubectl create -f deployments/fluentbit-config.yml
	kubectl create -f deployments/fluentbit-deploy.yml

delete:
	kubectl delete -f deployments/fluentbit-deploy.yml
	kubectl delete -f deployments/fluentbit-config.yml
