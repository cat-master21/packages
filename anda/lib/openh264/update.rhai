rpm.global("commit1", get("https://api.github.com/repos/mozilla/gmp-api/commits/HEAD").json().sha);
let h264 = gh("cisco/openh264");
h264.crop(1);
rpm.global("openh264_version", h264);
let html = get("https://gstreamer.freedesktop.org/src/gst-plugins-bad/?C=N;O=D");
rpm.global("gst_version", find("gst-plugins-bad-([\\d.]+).tar.xz", html, 1));
