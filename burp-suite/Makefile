# SMC Exploitation - Android Emulator Management
# Usage: make <command>

# Variables
AVD_NAME = SMC_Test_Device
PROXY_HOST = 127.0.0.1
PROXY_PORT = 8080
APP_PACKAGE = com.example.securechat

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help start stop restart status install-app uninstall-app logs cert-check clean

# Default target
help:
	@echo "$(GREEN)SMC Exploitation - Android Emulator Commands$(NC)"
	@echo ""
	@echo "$(YELLOW)Emulator Management:$(NC)"
	@echo "  make start          - Start emulator with proxy"
	@echo "  make stop           - Stop emulator"
	@echo "  make restart        - Restart emulator"
	@echo "  make status         - Check emulator status"
	@echo ""
	@echo "$(YELLOW)App Management:$(NC)"
	@echo "  make install-app    - Install patched APK"
	@echo "  make uninstall-app  - Uninstall app"
	@echo "  make launch-app     - Launch SecureChat app"
	@echo ""
	@echo "$(YELLOW)Debugging:$(NC)"
	@echo "  make logs           - Show app logs"
	@echo "  make cert-check     - Check Burp certificate"
	@echo "  make devices        - List connected devices"
	@echo ""
	@echo "$(YELLOW)Cleanup:$(NC)"
	@echo "  make clean          - Kill all emulator processes"

# Start emulator with proxy
start:
	@echo "$(GREEN)Starting Android Emulator with Burp Proxy...$(NC)"
	@pkill -f emulator || true
	@sleep 2
	@emulator -avd $(AVD_NAME) -writable-system -http-proxy $(PROXY_HOST):$(PROXY_PORT) -no-snapshot-load &
	@echo "$(YELLOW)Waiting for device to boot...$(NC)"
	@adb wait-for-device
	@echo "$(GREEN)Emulator started successfully!$(NC)"

# Stop emulator
stop:
	@echo "$(RED)Stopping Android Emulator...$(NC)"
	@pkill -f emulator || true
	@adb kill-server || true
	@echo "$(GREEN)Emulator stopped.$(NC)"

# Restart emulator
restart: stop
	@sleep 3
	@make start

# Check emulator status
status:
	@echo "$(YELLOW)Checking emulator status...$(NC)"
	@if pgrep -f emulator > /dev/null; then \
		echo "$(GREEN)✓ Emulator is running$(NC)"; \
		adb devices; \
	else \
		echo "$(RED)✗ Emulator is not running$(NC)"; \
	fi

# Install patched APK
install-app:
	@echo "$(GREEN)Installing SecureChat (patched)...$(NC)"
	@adb wait-for-device
	@adb uninstall $(APP_PACKAGE) 2>/dev/null || true
	@adb install 02-apk-files/secure-app-patched.apk
	@echo "$(GREEN)App installed successfully!$(NC)"

# Uninstall app
uninstall-app:
	@echo "$(RED)Uninstalling SecureChat...$(NC)"
	@adb uninstall $(APP_PACKAGE)
	@echo "$(GREEN)App uninstalled.$(NC)"

# Launch app
launch-app:
	@echo "$(GREEN)Launching SecureChat...$(NC)"
	@adb shell monkey -p $(APP_PACKAGE) -c android.intent.category.LAUNCHER 1

# Show app logs
logs:
	@echo "$(YELLOW)Showing SecureChat logs (Ctrl+C to stop)...$(NC)"
	@adb logcat -d | grep -i "securechat\|ssl\|certificate" || echo "No relevant logs found"

# Check Burp certificate installation
cert-check:
	@echo "$(YELLOW)Checking Burp certificate installation...$(NC)"
	@adb shell ls -la /system/etc/security/cacerts/ | grep 9a5ba575 || echo "$(RED)Certificate not found$(NC)"

# List connected devices
devices:
	@echo "$(YELLOW)Connected devices:$(NC)"
	@adb devices

# Setup root and remount (for certificate installation)
setup-root:
	@echo "$(GREEN)Setting up root access...$(NC)"
	@adb root
	@adb remount
	@echo "$(GREEN)Root access configured. Reboot required.$(NC)"

# Install Burp certificate
install-cert:
	@echo "$(GREEN)Installing Burp certificate...$(NC)"
	@adb root
	@adb remount
	@adb push 01-setup/9a5ba575.0 /system/etc/security/cacerts/
	@adb shell chmod 644 /system/etc/security/cacerts/9a5ba575.0
	@echo "$(YELLOW)Certificate installed. Rebooting device...$(NC)"
	@adb reboot
	@adb wait-for-device
	@echo "$(GREEN)Certificate installation complete!$(NC)"

# Quick start (start emulator + install app)
quick-start: start install-app
	@echo "$(GREEN)Quick start complete! Emulator running with app installed.$(NC)"

# Clean up all processes
clean:
	@echo "$(RED)Cleaning up all emulator processes...$(NC)"
	@pkill -f emulator || true
	@pkill -f adb || true
	@adb kill-server || true
	@echo "$(GREEN)Cleanup complete.$(NC)"

# Development workflow
dev: start install-app launch-app
	@echo "$(GREEN)Development environment ready!$(NC)"
	@echo "$(YELLOW)Emulator: Running with proxy$(NC)"
	@echo "$(YELLOW)App: Installed and launched$(NC)"
	@echo "$(YELLOW)Ready for Burp Suite interception!$(NC)"