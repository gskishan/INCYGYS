class CustomNotificationsView extends frappe.views.BaseNotificationsView {
    make() {
        super.make();

        // Call methods to create and style unread count element
        this.createUnreadCountElement();
        this.applyUnreadCountStyles();

        // Fetch notifications and display unread count
        this.get_notifications_list(this.max_length).then((r) => {
            if (!r.message) return;
            this.dropdown_items = r.message.notification_logs;
            frappe.update_user_info(r.message.user_info);
            this.render_notifications_dropdown();
            this.display_unread_count();
        });
    }

    createUnreadCountElement() {
        // Create the unread count span element
        this.unreadCountElement = document.createElement('span');
        this.unreadCountElement.classList.add('unread-count');
        this.notifications_icon[0].appendChild(this.unreadCountElement);
    }

    applyUnreadCountStyles() {
        // Apply CSS styles to the unread count element
        $(this.unreadCountElement).css({
            "position": "absolute",
            "top": "-10px",
            "right": "-10px",
            "background-color": "red",
            "color": "white",
            "border-radius": "50%",
            "padding": "2px 6px",
            "font-size": "12px",
            "font-weight": "bold",
            "display": "none"
        });
    }

    display_unread_count() {
        // Calculate and display the unread notification count
        let unreadCount = this.dropdown_items.filter(item => !item.read).length;
        if (unreadCount > 0) {
            $(this.unreadCountElement).text(unreadCount).css("display", "block");
        } else {
            $(this.unreadCountElement).css("display", "none");
        }
    }

    // Override or add other existing methods if needed
}

// Ensure this class is loaded instead of the original class
frappe.views.NotificationsView = CustomNotificationsView;
