# diskjockey

Disk Jockey is a Python tool to make it easier to imagize and preserve media such as floppy disks and optical media. Disk Jockey will assign a disk ID to each imagized disk, and store metadata with the image for future reference.

This is a work-in-progress. I do not suggest using it yet.

## TODO

### Short-term

- [x] Imagize media from a block device
- [ ] Collect metadata
    - [ ] Filesystem type
    - [ ] Label
    - [ ] Directory listing
    - [ ] Free-form text notes
- [ ] Post-imagizing command(s) (antivirus scan, compression, etc.)

### Medium-term

- [ ] Read configuration from a dotfile
- [ ] Select different commands to do the imagizing (dd, ddrescue, pv, etc.)
- [ ] Detect and log read errors
- [ ] Query metadata to locate images

### Long-term (or never)

- [ ] Support multiple pre and post commands
- [ ] Store metadata and notes in sqlite DB