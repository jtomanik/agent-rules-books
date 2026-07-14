The release is tomorrow. A new enterprise customer needs a one-off invoice
path. The proposed patch adds `enterpriseMode` to four public methods, a
`EnterpriseInvoiceHelper` that forwards to the existing service, and conditionals
in six callers. Reviewers are told to accept it because it is small, familiar,
and can be cleaned up after launch.

The enterprise difference is one alternate eligibility rule and one extra
document produced after a successful invoice. Existing callers should not need
to know either detail.

Decide whether to approve the patch under schedule pressure. Give the smallest
design correction that prevents caller coordination, shallow abstraction, and
special-case spread without turning the task into a broad rewrite.
