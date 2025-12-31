// Copyright (c) 2025, suman and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Doc One", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Doc One", {
	refresh(frm) {

	},
    get_summary(frm){
        
        let txt = "<h1>"+frm.doc.last_name+"</h1>";

        frm.get_field("summary").$wrapper.html(txt)
    }
    //cur_frm.get_field("summary").$wrapper.append("hi")

});

