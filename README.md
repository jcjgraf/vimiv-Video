## Vimiv Video
> [vimiv](https://github.com/karlch/vimiv-qt) plugin for video support

vimiv Video enables support for videos. Videos get listed within vimiv and can be played using an external player like [mpv](https://mpv.io/) or [vlc](https://www.videolan.org/vlc/).

### Supported Formats
The following video formats are currently supported:

| **Format**                   | **Extension** |
| :---                         | :---:         |
| MPEG-4                       | `.mp4`        |
| QuickTime Movie              | `.mov`        |
| Audio Video Interleave (AVI) | `.avi`        |

### Installation
- This plugin requires [ffmpeg](https://ffmpeg.org/) which needs to be installed.
- Clone this project into `$XDG_DATA_HOME/vimiv/plugins/`
- Activate vimiv Video by adding `video =` to the `PLUGINS` section of `$XDG_CONFIG_HOME/vimiv/vimiv.conf`.

### Usage
All your videos are automatically listed in vimiv. To play the selected video, type something like `:!mpv %`.

### Contribute
If you would like to add support for a new video file format feel free to open a PR with the appropriate additions. In case you do not know how to implement it, you are also welcome to open an issue and submit an adequate sample file.
