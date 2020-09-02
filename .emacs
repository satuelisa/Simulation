;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)


;; make sure file is visible to emacs (if needed)
(add-to-list 'load-path "/Users/elisa/.emacs.d/lisp/")

;; load the file
(require 'gnuplot-mode)

;; specify the gnuplot executable (if other than /usr/bin/gnuplot)
(setq gnuplot-program "/sw/bin/gnuplot")

;; automatically open files ending with .gp or .gnuplot in gnuplot mode
(setq auto-mode-alist 
(append '(("\\.\\(gp\\|gnuplot\\)$" . gnuplot-mode)) auto-mode-alist))


(defun replace-accents-html ()
  (interactive)
  (replace-string "á" "&aacute;" nil (point-min) (point-max))
  (replace-string "é" "&eacute;" nil (point-min) (point-max))
  (replace-string "í" "&iacute;" nil (point-min) (point-max))
  (replace-string "ó" "&oacute;" nil (point-min) (point-max))
  (replace-string "ú" "&uacute;" nil (point-min) (point-max))
  (replace-string "ñ" "&ntilde;" nil (point-min) (point-max))
  (replace-string "Á" "&Aacute;" nil (point-min) (point-max))
  (replace-string "É" "&Eacute;" nil (point-min) (point-max))
  (replace-string "Í" "&Iacute;" nil (point-min) (point-max))
  (replace-string "Ó" "&Oacute;" nil (point-min) (point-max))
  (replace-string "Ú" "&Uacute;" nil (point-min) (point-max))
  (replace-string "Ñ" "&Ntilde;" nil (point-min) (point-max)))


(defun replace-accents-ascii ()
  (interactive)
  (replace-string "á" "a" nil (point-min) (point-max))
  (replace-string "é" "e" nil (point-min) (point-max))
  (replace-string "í" "i" nil (point-min) (point-max))
  (replace-string "ó" "o" nil (point-min) (point-max))
  (replace-string "ú" "u" nil (point-min) (point-max))
  (replace-string "ñ" "n" nil (point-min) (point-max))
  (replace-string "Á" "A" nil (point-min) (point-max))
  (replace-string "É" "E" nil (point-min) (point-max))
  (replace-string "Í" "I" nil (point-min) (point-max))
  (replace-string "Ó" "O" nil (point-min) (point-max))
  (replace-string "Ú" "U" nil (point-min) (point-max))
  (replace-string "Ñ" "N" nil (point-min) (point-max)))


(defun replace-accents-latex ()
  (interactive)
  (replace-string "á" "\\'{a}" nil (point-min) (point-max))
  (replace-string "é" "\\'{e}" nil (point-min) (point-max))
  (replace-string "í" "\\'{\\i}" nil (point-min) (point-max))
  (replace-string "ó" "\\'{o}" nil (point-min) (point-max))
  (replace-string "ú" "\\'{u}" nil (point-min) (point-max))
  (replace-string "ñ" "\\~{n}" nil (point-min) (point-max))
  (replace-string "Á" "\\'{A}" nil (point-min) (point-max))
  (replace-string "É" "\\'{E}" nil (point-min) (point-max))
  (replace-string "Í" "\\'{\\I}" nil (point-min) (point-max))
  (replace-string "Ó" "\\'{O}" nil (point-min) (point-max))
  (replace-string "Ú" "\\'{U}" nil (point-min) (point-max))
  (replace-string "Ñ" "\\~{N}" nil (point-min) (point-max)))


(add-hook 'LaTeX-mode-hook
          '(lambda ()
             (setq ispell-tex-skip-alists
                   (list
                    (append
                     (car ispell-tex-skip-alists) 
                     '(("[^\\]\\$" . "[^\\]\\$")))
                    (cadr ispell-tex-skip-alists))) ))
(put 'downcase-region 'disabled nil)


(defun find-next-unsafe-char (&optional coding-system)
  "Find the next character in the buffer that cannot be encoded by
coding-system. If coding-system is unspecified, default to the coding
system that would be used to save this buffer. With prefix argument,
prompt the user for a coding system."
  (interactive "Zcoding-system: ")
  (if (stringp coding-system) (setq coding-system (intern coding-system)))
  (if coding-system nil
    (setq coding-system
          (or save-buffer-coding-system buffer-file-coding-system)))
  (let ((found nil) (char nil) (csets nil) (safe nil))
    (setq safe (coding-system-get coding-system 'safe-chars))
    ;; some systems merely specify the charsets as ones they can encode:
    (setq csets (coding-system-get coding-system 'safe-charsets))
    (save-excursion
      ;;(message "zoom to <")
      (let ((end  (point-max))
            (here (point    ))
            (char  nil))
        (while (and (< here end) (not found))
          (setq char (char-after here))
          (if (or (eq safe t)
                  (< char ?\177)
                  (and safe  (aref safe char))
                  (and csets (memq (char-charset char) csets)))
              nil ;; safe char, noop
            (setq found (cons here char)))
          (setq here (1+ here))) ))
    (and found (goto-char (1+ (car found))))
    found))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(show-paren-mode t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
