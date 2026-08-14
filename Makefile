all: sync

sync:
	git add .
	git commit -m "Auto-sync telemetry pipeline heartbeat: $(shell date +'%Y-%m-%d %H:%M:%S')" || true
	git push origin main || true
