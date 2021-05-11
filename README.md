## Vimiv Video
> [vimiv](https://github.com/karlch/vimiv-qt) plugin for video support

Vimiv Video enables support for videos. Videos get listed within vimiv and can be played using an external player like [mpv](https://mpv.io/) or [vlc](https://www.videolan.org/vlc/).

### Supported Formats
The following video formats are currently supported:

| **Format**                   | **Extension** |
| :---                         | :---:         |
| MPEG-4                       | `.mp4`        |
| QuickTime Movie              | `.mov`        |
| Audio Video Interleave (AVI) | `.avi`        |

### Installation
- This plugin requires `ffmpeg` which needs to be installed.
- Clone this project into `$XDG_DATA_HOME/vimiv/plugins/`
- Activate Vimiv Video by adding `video =` to the `PLUGINS` section of `$XDG_CONFIG_HOME/vimiv/vimiv.conf`.

### Usage
All your videos are automatically listed in vimiv. To play the currently selected video, type something like `:!mpv %`.

### Contribute
If you would like support for a new video format feel free to open a PR with the appropriate additions. In case you do not know how this is implemented, you are also very welcome to open an issue and submit an adequate sample file.

Let me also know if you detect some inconsistencies with the type detection. I.e. a non-video file is being detected as a video or vice-versa.
